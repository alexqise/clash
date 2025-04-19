import Link from "next/link"
import Image from "next/image"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Shield, Swords, Trophy, BrainCircuit } from "lucide-react"

export default function HomePage() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <header className="bg-blue-900 text-white shadow-md">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <Trophy className="h-8 w-8 text-yellow-400" />
            <h1 className="text-xl md:text-2xl font-bold">Clash Counter Academy</h1>
          </div>
          <nav className="hidden md:flex gap-6">
            <Link href="/" className="hover:text-yellow-400 font-medium">
              Home
            </Link>
            <Link href="/learn" className="hover:text-yellow-400 font-medium">
              Learn
            </Link>
            <Link href="/quiz" className="hover:text-yellow-400 font-medium">
              Quiz
            </Link>
            <Link href="/about" className="hover:text-yellow-400 font-medium">
              About
            </Link>
          </nav>
          <Button variant="outline" className="md:hidden bg-transparent border-white text-white hover:bg-blue-800">
            Menu
          </Button>
        </div>
      </header>

      {/* Hero Section */}
      <section className="bg-gradient-to-b from-blue-800 to-blue-900 text-white py-12 md:py-20">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-3xl md:text-5xl font-bold mb-4">Master Win Condition Counters</h1>
          <p className="text-lg md:text-xl max-w-2xl mx-auto mb-8">
            Learn how to effectively counter every win condition in Clash Royale and climb the ladder.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button asChild size="lg" className="bg-yellow-500 hover:bg-yellow-600 text-black">
              <Link href="/learn">Start Learning</Link>
            </Button>
            <Button asChild size="lg" variant="outline" className="border-white text-white hover:bg-blue-800">
              <Link href="/quiz">Test Your Knowledge</Link>
            </Button>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-12 md:py-20 bg-gray-100">
        <div className="container mx-auto px-4">
          <h2 className="text-2xl md:text-3xl font-bold text-center mb-12">Why Learn With Us?</h2>

          <div className="grid md:grid-cols-3 gap-8">
            <Card>
              <CardHeader>
                <Shield className="h-12 w-12 text-blue-600 mb-2" />
                <CardTitle>Defense Mastery</CardTitle>
              </CardHeader>
              <CardContent>
                <p>Learn optimal defensive placements and timing against every win condition in the game.</p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <Swords className="h-12 w-12 text-red-600 mb-2" />
                <CardTitle>Counter Attacks</CardTitle>
              </CardHeader>
              <CardContent>
                <p>Turn your defenses into powerful counter pushes that will catch your opponents off guard.</p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <BrainCircuit className="h-12 w-12 text-purple-600 mb-2" />
                <CardTitle>Interactive Learning</CardTitle>
              </CardHeader>
              <CardContent>
                <p>Test your knowledge with quizzes and scenarios to reinforce what you've learned.</p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Win Conditions Preview */}
      <section className="py-12 md:py-20">
        <div className="container mx-auto px-4">
          <h2 className="text-2xl md:text-3xl font-bold text-center mb-4">Win Conditions Covered</h2>
          <p className="text-center text-gray-600 max-w-2xl mx-auto mb-12">
            Our comprehensive guides cover all the major win conditions you'll face on ladder and in challenges.
          </p>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
            {["Hog Rider", "Royal Giant", "Golem", "Balloon", "Goblin Barrel", "Giant", "PEKKA", "Graveyard"].map(
              (card) => (
                <Card key={card} className="overflow-hidden">
                  <div className="aspect-square relative bg-gray-200">
                    <Image
                      src={`/placeholder.svg?height=200&width=200&text=${encodeURIComponent(card)}`}
                      alt={card}
                      fill
                      className="object-cover"
                    />
                  </div>
                  <CardFooter className="p-2 justify-center">
                    <p className="font-medium text-sm">{card}</p>
                  </CardFooter>
                </Card>
              ),
            )}
          </div>

          <div className="text-center mt-8">
            <Button asChild variant="outline">
              <Link href="/learn">View All Win Conditions</Link>
            </Button>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="bg-blue-900 text-white py-12">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-2xl md:text-3xl font-bold mb-4">Ready to Improve Your Game?</h2>
          <p className="max-w-2xl mx-auto mb-8">
            Start learning today and see your trophy count rise as you master the art of countering win conditions.
          </p>
          <Button asChild size="lg" className="bg-yellow-500 hover:bg-yellow-600 text-black">
            <Link href="/learn">Get Started Now</Link>
          </Button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center gap-2 mb-4 md:mb-0">
              <Trophy className="h-6 w-6 text-yellow-400" />
              <span className="text-lg font-bold">Clash Counter Academy</span>
            </div>
            <div className="flex gap-6">
              <Link href="/" className="hover:text-yellow-400">
                Home
              </Link>
              <Link href="/learn" className="hover:text-yellow-400">
                Learn
              </Link>
              <Link href="/quiz" className="hover:text-yellow-400">
                Quiz
              </Link>
              <Link href="/about" className="hover:text-yellow-400">
                About
              </Link>
            </div>
          </div>
          <div className="mt-6 text-center md:text-left text-gray-400 text-sm">
            <p>© {new Date().getFullYear()} Clash Counter Academy. Not affiliated with Supercell.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
